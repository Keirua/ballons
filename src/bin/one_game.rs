extern crate ballonslib;
use ballonslib::game::BalloonGame;

use structopt::StructOpt;

#[derive(Debug, StructOpt)]
#[structopt(about = "Running multiple game iterations.")]
struct Opt {
    /// number of players
    #[structopt(short = "n", long = "nb_players", default_value = "2")]
    nb_players: usize,

    /// number of cards per player
    #[structopt(short = "c", long = "nb_cards", default_value = "5")]
    nb_cards: usize,

    /// number of parent cards
    #[structopt(short = "p", long = "nb_parents", default_value = "5")]
    nb_parents: usize,
}

fn main() {
    let opt = Opt::from_args();
    let mut balloon_game = BalloonGame::new(opt.nb_players, opt.nb_cards, opt.nb_parents);

    println!("{}", balloon_game.run_game());
}
