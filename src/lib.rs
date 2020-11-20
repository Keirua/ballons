extern crate rand;

mod ballons;
mod deck;
pub mod game;
mod player;


use crate::game::BalloonGame;

#[no_mangle]
pub extern "C" fn run_balloon_game(nb_players: usize, nb_cards: usize, nb_parents: usize) -> usize {
  let mut balloon_game = BalloonGame::new(nb_players, nb_cards, nb_parents);
  balloon_game.run_game()
}
