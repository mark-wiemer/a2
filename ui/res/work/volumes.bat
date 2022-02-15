@REM set magick="C:\Program Files\ImageMagick\magick.exe"
set inkscape="C:\Program Files\Inkscape\bin\inkscape.exe"

set name=volume_up
%inkscape% --export-type=png --export-dpi=200 --export-background-opacity=0 ..\%name%.svg
move ..\%name%.png %name%.png
magick %name%.png -resize 48x48 %name%48.png
magick %name%.png -resize 16x16 %name%16.png
magick convert %name%16.png %name%48.png ..\%name%.ico

set name=volume_down
%inkscape% --export-type=png --export-dpi=200 --export-background-opacity=0 ..\%name%.svg
move ..\%name%.png %name%.png
magick %name%.png -resize 48x48 %name%48.png
magick %name%.png -resize 16x16 %name%16.png
magick convert %name%16.png %name%48.png ..\%name%.ico
