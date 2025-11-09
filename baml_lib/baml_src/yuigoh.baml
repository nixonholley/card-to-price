// Defining a data model.
class YugiohCard {
  name string @description(#"
    Name of the card, located at the upper-left corner.
  "#)

  type string @description(#"
    Card classification, located in the top-right corner inside a colored attribute box.
    Examples: 'Dragon / Effect', 'Spell Card', 'Trap Card'.
  "#)

  stars int @description(#"
    Number of Level/Ranks stars displayed directly under the name section.
  "#)

  ATK int @description(#"
    Attack value located in the bottom-right stat box.
  "#)

  DEF int @description(#"
    Defense value located next to ATK in the stat box.
  "#)

  description string @description(#"
    The effect text printed beneath the artwork. May contain rules text,
    flavor text, or both.
  "#)

  card_number string @description(#"
    The set ID found below the artwork (usually bottom-right), e.g. 'LOB-001'.
    Indicates set, region, and card number within that set.
  "#)

  video_game_identifier int @description(#"
    The 8-digit Konami card ID located in the lower-left corner. Used
    for video game and database indexing.
  "#)

  edition string?  @description(#"
    Text indicating printing edition (e.g., '1st Edition', 'Unlimited Edition').
  "#)
}

// Image processing function
function ExtractYugiohCardFromImage(img: image) -> YugiohCard {
    client CustomGPT4
    prompt #"       
        {{_.role("user")}}

        Extract details from this image of a Yu-Gi-Oh! Card.
        
        Image : {{ img }}

        {{ ctx.output_format }}
    "#
}



test Test_Blue_Eyes_White_Dragon {
functions [ExtractYugiohCardFromImage]
  args {
    img {
      file "./index12.jpg"
    }
  }
}
