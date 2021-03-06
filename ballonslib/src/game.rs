use crate::ballons::Balloons;
use crate::deck::{ActionDeck, BalloonDeck};
use crate::player::Player;

use rand::rngs::ThreadRng;
use rand::thread_rng;

#[derive(Debug)]
pub struct BalloonGame {
    nb_players: usize,
    nb_balloons_per_player: usize,
    pub players: Vec<Player>,
    action_deck: ActionDeck,
    rng: ThreadRng,
}

impl BalloonGame {
    pub fn new(
        nb_players: usize,
        nb_parent_cards: usize,
        nb_balloons_per_player: usize,
    ) -> BalloonGame {
        let rng = thread_rng();

        let mut balloon_game = BalloonGame {
            nb_players,
            nb_balloons_per_player,
            players: Vec::with_capacity(nb_players),
            action_deck: ActionDeck::new(nb_parent_cards, rng),
            rng,
        };

        for _ in 0..nb_players {
            balloon_game.players.push(Player::default());
        }
        balloon_game.deal_cards();
        balloon_game.action_deck.shuffle();

        balloon_game
    }

    pub fn new_with_known_hands(hand1: Vec<Balloons>, hand2: Vec<Balloons>) -> BalloonGame {
        let rng = thread_rng();

        let mut players = Vec::with_capacity(2);
        players.push(Player::new_with_hand(hand1));
        players.push(Player::new_with_hand(hand2));

        let mut balloon_game = BalloonGame {
            nb_players: 2,
            nb_balloons_per_player: 5,
            players,
            action_deck: ActionDeck::new(5, rng),
            rng,
        };

        balloon_game.action_deck.shuffle();

        balloon_game
    }

    pub fn new_with_known_hands_and_counter(hand1: Vec<Balloons>, hand2: Vec<Balloons>) -> BalloonGame {
        let mut game = BalloonGame::new_with_known_hands(hand1, hand2);
        game.players[0].set_counter(true);

        balloon_game
    }

    fn deal_cards(&mut self) {
        let mut balloon_deck = BalloonDeck::new(self.rng);
        balloon_deck.shuffle();

        for p in 0..self.nb_players {
            for _ in 0..self.nb_balloons_per_player {
                if let Some(b) = balloon_deck.cards.pop() {
                    self.players[p].deal(b);
                }
            }
        }
    }

    pub fn run_game(&mut self) -> usize {
        let mut nb_cards = 0;
        let mut current_player_index = 0;

        loop {
            let p = &mut self.players[current_player_index];
            let action = self.action_deck.deal();
            p.play_card(action);
            nb_cards += 1;
            if p.has_lost() {
                return nb_cards;
            } else {
                for player in self.players.iter_mut() {
                    player.notify(action);
                }
                current_player_index = (current_player_index + 1) % self.players.len();
            }
        }
    }
}
