
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

; Additional icons for LongTurn-specific units.

artists = "
    Hugo Flavio (by editing icons present in the regular Amplio2 pack and other modpacks)
    Daavko <david.konir@gmail.com>
"

[file]
gfx = "hexemplioLT/units_LT"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
        ; Scenario League tags in brackets
  0, 0, "u.barge"    ; modded_by_HF
  0, 1, "u.tribal_worker"   ; modded_by_HF
  0, 2, "u.immigrant"  ; modded_by_HF
  0, 3, "u.scribe"     ; modded_by_HF
  0, 4, "u.scholar"    ; modded_by_HF
  0, 5, "u.inventor"   ; modded_by_HF
  0, 6, "u.scientist"  ; modded_by_HF
  0, 7, "u.infantry"   ; modded_by_HF
  0, 8, "u.operative"  ; modded_by_HF
  0, 9, "u.nsubmarine" ; modded_by_HF
  0, 9, "u.nsubmarinetii" ; same sprite as u.nsubmarine used for now
  0, 10, "u.fusion_bomber" ; modded_by_HF
  0, 11, "u.fusion_armor" ; Sketlux
  0, 12, "u.nuclearbomb" ; Sketlux
  0, 13, "u.fusion_fighter" ; Sketlux
  0, 14, "u.fusion_battleship" ; Sketlux
  0, 15, "u.cargoair" ; Sketlux (XYZ)
  1, 0, "u.longboat"  ; modded_by_HF
  1, 1, "u.srcaravel" ; modded_by_HF
  1, 2, "u.missile" ; [CS]
  1, 3, "u.cruise_missile" ; [CS] & [Lexxie]
  1, 4, "u.fusion_missile" ; modded from the above by HF
  1, 5, "u.trebuchet" ; HF & louis94
  1, 6, "u.navytroops" ; Sketlux (XYZ)
  2, 0, "u.pirogue"   ; Ngunjaca
  2, 1, "u.cog"       ; Ngunjaca
  2, 2, "u.pcutter"   ; VladimirSlavik
  2, 3, "u.flagship_frigate" ; modded_by_Sketlux (XYZ)
  2, 4, "u.atorpedo" ; modded from Freeciv Nuclear sprite by Daavko
  }
