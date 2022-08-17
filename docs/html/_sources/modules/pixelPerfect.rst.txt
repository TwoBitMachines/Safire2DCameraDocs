Pixel Perfect
+++++++++++++

Event though Unity already has a Pixel Perfect Camera, this module will be kept 
for the completeness of the engine.

This module is intended for use with orthographic cameras. Before starting your game, 
choose the resolution the game will be designed for. By default it’s set to 320x180 since 
it can multiply nicely into common device resolutions. This will determine how much of 
the game world the user can view as determined by the PPU of your game art; changing this
resolution later might change the look and feel of the game, so choose
wisely.

The camera will execute in Edit Mode and create black bars automatically 
for any screen resolution that is not pixel perfect.

It is recommended to use a separate camera for UI. Add the PixelPerfectUI component to the UI
camera. Make sure the UI camera is only rendering the UI layer. On the flip side, the main camera should not
render the UI layer. Match the PPU and resolution settings. On any canvas in your game world, set 
the render mode to Screen Space - Camera and set the UI camera as a reference. Set Canvas Scaler to scale 
with screen size and set the target resolution. Set the UI camera depth to a larger 
value than the main camera so it renders on top of it. And finally, set the clear flags to Don't Clear.

Typically you shouldn't zoom with a pixel perfect camera as it will break pixel perfectness. But if you do, zoom by integer multiples 
if possible to retain a pixel perfect screen.

All your sprites should strive to have the same PPU settings and bet set to Point filter with no compression.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - PPU
     - This is the PPU (Pixel Per Unit) of the game art. How many pixels fit in one world unit of the game? 
       The Wrench Button, if clicked, will snap all scene objects to the PPU grid. The color will change the color 
       of the black bars.

   * - Resolution
     - The target size of your game world.
