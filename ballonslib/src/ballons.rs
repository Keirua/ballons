#[derive(Debug, PartialEq, Eq, Hash, Copy, Clone)]
pub enum Balloons {
    Red,
    Blue,
    Green,
    Violet,
    Yellow,
}

impl From<usize> for Balloons {
    fn from(ballon: usize) -> Self {
        match ballon {
            0 => Balloons::Red,
            1 => Balloons::Blue,
            2 => Balloons::Green,
            3 => Balloons::Violet,
            4 => Balloons::Yellow,
            _ => unreachable!(format!("this conversion attempt should never happen: {}", ballon))
        }
    }
}

#[derive(Debug, PartialEq, Eq, Hash, Copy, Clone)]
pub enum ActionCard {
    Red,
    Blue,
    Green,
    Violet,
    Yellow,
    Parent,
}
