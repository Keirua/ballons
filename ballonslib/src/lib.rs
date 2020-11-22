extern crate rand;
extern crate libc;

mod ballons;
mod deck;
pub mod game;
mod player;

use crate::ballons::Balloons;
use crate::game::BalloonGame;
use libc::size_t;

/// Run a game with 2 random hands, and return the game length after random play from both players
#[no_mangle]
pub extern "C" fn run_balloon_game(nb_players: usize, nb_cards: usize, nb_parents: usize) -> usize {
    let mut balloon_game = BalloonGame::new(nb_players, nb_cards, nb_parents);
    balloon_game.run_game()
}

/// Run a game with 2 known hands, and return true if the first player won the game, false otherwise
/// both players play randomly
/// # Safety
///
/// This function may read from unallocated memory
#[allow(clippy::not_unsafe_ptr_arg_deref)]
#[no_mangle]
pub extern "C" fn run_game_with_known_hand(
    hand1: *const u32,
    hand2: *const u32,
    len: size_t,
) -> bool {
    let hand1 = unsafe {
        assert!(!hand1.is_null());
        std::slice::from_raw_parts(hand1, len)
    };

    let hand2 = unsafe {
        assert!(!hand2.is_null());
        std::slice::from_raw_parts(hand2, len)
    };

    let hand1: Vec<Balloons> = hand1.iter().map(|balloon| (*balloon as usize).into()).collect();
    let hand2: Vec<Balloons> = hand2.iter().map(|balloon| (*balloon as usize).into()).collect();

    let mut balloon_game = BalloonGame::new_with_known_hands(hand1, hand2);

    balloon_game.run_game();

    !balloon_game.players[0].has_lost()
}


/// Run a game with 2 known hands, and return true if the first player won the game, false otherwise
/// the first player is counting cards, while the second one is playing randomly
/// # Safety
///
/// This function may read from unallocated memory
#[allow(clippy::not_unsafe_ptr_arg_deref)]
#[no_mangle]
pub extern "C" fn run_game_with_known_hand_and_counter(
    hand1: *const u32,
    hand2: *const u32,
    len: size_t,
) -> bool {
    let hand1 = unsafe {
        assert!(!hand1.is_null());
        std::slice::from_raw_parts(hand1, len)
    };

    let hand2 = unsafe {
        assert!(!hand2.is_null());
        std::slice::from_raw_parts(hand2, len)
    };

    let hand1: Vec<Balloons> = hand1.iter().map(|balloon| (*balloon as usize).into()).collect();
    let hand2: Vec<Balloons> = hand2.iter().map(|balloon| (*balloon as usize).into()).collect();

    let mut balloon_game = BalloonGame::new_with_known_hands_and_counter(hand1, hand2);

    balloon_game.run_game();

    !balloon_game.players[0].has_lost()
}
