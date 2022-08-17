Follow
++++++

Implement standard camera mechanics for following the target. Mix and match these properties where it makes sense to do so.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Speed
     - How fast the camera should follow the target.

   * - Smooth
     - The camera will smooth towards the target. 
       A value of zero halts the camera. A value of one instantly moves the camera to the target’s position.

   * - Offset
     - Offset the target’s follow position in the x or y axis.

   * - Dead Zone
     - The area surrounding the target in which no target movement is detected by the camera.
 
   * - Screen Zone
     - Prevent the target from escaping the camera view. This occurs when the target is moving too fast or when the 
       camera is moving too slow.

   * - Auto Scroll
     - Scroll the camera with the specified speed. Setting any axis here will override the other mechanics in that axis

   * - Detect Walls
     - If None is enabled, the system will ignore this setting. If Ignore Gravity is enabled, the camera will not follow the target when it's jumping.
       If Detect Walls is enabled, the camera will only follow the target if it's touching a surface. Specify the layer that represents hard surfaces in your world.
       This mechanic assumes the target contains a BoxCollider2D. Enable this by method. 0 == Node, 1 == IgnoreGravity, 2 == DetectWalls.

   * - Push Zone
     - Force the camera to follow the target only in the desired direction. For example, if Push Zone X is set to Push Left, the camera will ignore the target if it’s
       moving to the right. The value represents where in the screen the camera will begin to follow the target. Do note, the camera will ease into the push zone to prevent 
       abrupt target changes.

.. list-table::
   :widths: 75 100
   :header-rows: 1

   * - Method
     -
     
   * - ChangeTargetTransform (Transform newTransform)
     -

   * - CenterCameraOnTarget ( )
     -

   * - SetCameraPosition (Vector3 position)
     -

   * - SetFollowSpeed (float speed)
     -

   * - SetFollowSmooth (Vector2 smooth)
     -

   * - SetAutoScrollSpeed (Vector2 speed)
     -

   * - PauseAutoScroll (bool enable)
     -

   * - DetectWallsSet (int key)
     -