Rails
+++++

The camera moves in a segmented path as it follows the target. A segmented path consists of targets that you must 
place in the scene. The first and last targets will be the triggers. Once the target enters a trigger, the camera begins 
to follow the rail path. This requires the Follow module to be enabled.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Name
     - The name of the rail for identification purposes (optional).

   * - Horizontal
     - The camera follows the target’s horizontal position. 
       This rail shouldn’t have vertical segments.

   * - Vertical
     - The camera follows the target’s vertical position. 
       This rail shouldn’t have horizontal segments.

   * - Auto
     - The camera completely ignores the target’s position and follows the segmented path at a
       specified speed. The automatic rail contains a Unity Event that is 
       invoked when it completes the path.

   * - RailPause (bool value)
     - Pause or unpause an active auto rail.
