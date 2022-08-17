User
++++

Instead of having the camera follow the target, the camera is
controlled directly by the user using touch, the keyboard, and mouse
input. Switch the follow type from Target to User.

When the follow type is User, the system is using the center of the camera 
as the target. Thus, this mode isn't compatible with the following modules:
Dead Zone, Look Ahead, Follow Blocks, Multiple Targets, Regions, Screen Zone, Push Zone, and Peek.

-----------

Pan
===

This controls the camera movement. Use Touch, Mouse, or Keyboard
input to move the camera. 

If a touch or mouse position is at the edge of
the camera, Pan Edge will move the camera automatically in that
direction. Choose how big the area will be to detect a touch or mouse
position near the edge of the camera. The Left, Right, Top, Bottom values
are percent values. A value of one will result in a distance that is half the
width of the camera. A value of zero will result in no edge detection. Use
the Damp value to reduce the speed of the pan edge.

-----------

Zoom
====

This controls the camera zoom level. Zoom with Touch, Mouse, or
Keyboard. The Range will determine the minimum and maximum zoom
levels. Speed and Smooth will control the rate of the zoom.

-----------

Rotate
======

This controls the camera rotation. Rotate with Touch, Mouse, or
Keyboard. Speed and Smooth will control the rate of rotation.

-----------

.. list-table::
   :widths: 100 50
   :header-rows: 1

   * - Method
     - 

   * - PauseUser (bool pausePan, bool pauseZoom, bool pauseRotate)
     - Pause a user module.

   * - UserPanKeyboard (KeyCode left, KeyCode right, KeyCode up, KeyCode down)
     - Change the user keyboard settings for pan movement. 

   * - UserPanMouse (Pan panType, MouseButton mouseButton, MouseButton holdButton)
     - Change the user mouse settings for pan movement.

   * - UserZoomKeyboard (KeyCode zoomInKey, KeyCode zoomOutKey)
     - Change the user keyboard settings for zooming.

   * - UserRotateKeyboard (KeyCode rotateLeftKey, KeyCode rotateRightKey)
     - Change the user keyboard settings for camera rotation. 
