use core::num;
use std::fs::read_to_string;
use std::collections::HashMap;
use std::cmp;
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;
use std::sync::{Arc, Mutex, RwLock};

struct Map {
    dest_start: i64,
    source_start: i64,
    range: i64,
}

#[derive(Debug, Copy, Clone)]
struct SeedRange {
    start: i64,
    range: i64,
}

fn main() {

    let mut range_vals: HashMap<&str,Vec<Map>> = HashMap::new();

    let mut key = "";
    let seeds_input = "858905075 56936593 947763189 267019426 206349064 252409474 660226451 92561087 752930744 24162055 75704321 63600948 3866217991 323477533 3356941271 54368890 1755537789 475537300 1327269841 427659734";
    //let seeds_input = "79 14 55 13";
    let mut sv = Vec::new();
    
    let mut temp_seed_vector = Vec::new();
    for v in seeds_input.split(" "){
        // println!("{}", v);
        let vint = v.parse::<i64>().unwrap();
        temp_seed_vector.push(vint);
    }
    for i in (0..temp_seed_vector.len()).step_by(2) {
        let sr = SeedRange {
            start: temp_seed_vector[i],
            range: temp_seed_vector[i + 1]
        };
        sv.push(sr);
    }
    println!("len of sv is: {}", sv.len());
    
    for line in read_to_string("./input.txt").unwrap().lines() {
        if line.contains("seeds:") {
            continue
        }
        // set the key
        if line.contains("seed-to-soil"){
            key = "s_to_s";
            continue
        }
        else if line.contains("soil-to-fertilizer") {
            key = "s_to_f";
            continue
        }
        else if line.contains("fertilizer-to-water") {
            key = "f_to_w";
            continue
        }
        else if line.contains("water-to-light") {
            key = "w_to_l";
            continue
        }
        else if line.contains("light-to-temperature") {
            key = "l_to_t";
            continue
        }
        else if line.contains("temperature-to-humidity") {
            key = "t_to_h";
            continue
        }
        else if line.contains("humidity-to-location") {
            key = "h_to_l";
            continue
        }
        // 
        if key != "" && line != "" {
            let mut tv = Vec::new();
            for v in line.split(" "){
                // println!("{}", v);
                let vint = v.parse::<i64>().unwrap();
                tv.push(vint);
            }
            let m = Map {
                dest_start: tv[0],
                source_start: tv[1],
                range: tv[2],
            };
            if !range_vals.contains_key(key) {
                range_vals.insert(key, Vec::new());
            }
            match range_vals.get_mut(key) {
                Some(vv) => vv.push(m),
                None => panic!("shouldn't have gotten here")
            }
        }
    }

    let num_threads = sv.len();
    let (tx, rx): (Sender<i64>, Receiver<i64>) = mpsc::channel();
    let mut children = vec![];

    let rvl = Arc::new(RwLock::new(range_vals));

    for threadnum in 0..num_threads {
        let range = sv[threadnum];
        let rvt = Arc::clone(&rvl);
        let thread_tx = tx.clone();
        let child = thread::spawn(move || {
            check_range(&range, rvt, thread_tx);
            
        });
        children.push(child);
    }
    // collect
    let mut mins = Vec::with_capacity(num_threads as usize);
    let mut gval = 0;
    for _ in 0..num_threads {
        mins.push(rx.recv().unwrap());
        println!("Got value from {}", gval);
        gval = gval + 1;
    }
    for child in children {
        child.join().expect("oops! the child thread panicked");
    }

    let mut min = std::i64::MAX;
    for cm in mins {
        min = cmp::min(min, cm)
    }
    println!("Final min: {}",min)

    // let mut min = std::i64::MAX;
    // for range in sv {
    //     let rmin = check_range(&range, &range_vals);
    //     min = cmp::min(min, rmin);
    // }
    // print!("{}",min)


}

fn get_map(key: &str, input: i64, map: &HashMap<&str,Vec<Map>>) -> i64 {
    for r in map.get(key) {
        for m in r {
            if input >= m.source_start && input < (m.source_start + m.range) {
                let delta = input - m.source_start;
                return m.dest_start + delta;
            }
        }
    }
    return input
}

fn check_range(sr: &SeedRange, arcmap: Arc<RwLock<HashMap<&str,Vec<Map>>>>, tx: Sender<i64>) {
    println!("Checking range from {} to {}", sr.start, sr.start+sr.range);
    let mut min = std::i64::MAX;
    let map = arcmap.read().expect("RwLock Poisoned");
    for seed in (sr.start..(sr.start+sr.range)) {
        let soil = get_map("s_to_s", seed, &map);
        let fert = get_map("s_to_f", soil, &map);
        let wate = get_map("f_to_w", fert, &map);
        let lite = get_map("w_to_l", wate, &map);
        let temp = get_map("l_to_t", lite, &map);
        let humi = get_map("t_to_h", temp, &map);
        let loca = get_map("h_to_l", humi, &map);
        min = cmp::min(min, loca);
    }
    tx.send(min);
}
