Peek
++++

This allows the user to quickly peek the camera in the desired direction. This is similar to look ahead, but 
with this module, the direction of the camera is controlled by the user and not by the target's direction. 

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Distance
     - The peek distance.

   * - Easing Time
     - The time it takes to reach the maximum peek distance.

   * - Ignore Clamps
     - If enabled, peek will ignore room clamps and the world clamp. Otherwise, it is clamped. 
       Be aware that sometimes the peek effect won't be noticeable if the camera itself is being 
       clamped if this option is disabled.

   * - Direction
     - If any of the buttons are pressed, the camera will peek in the desired direction. 
       Set to None if not required.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Method
     - Call these methods continuously to peek in the respective direction.

   * - PeekUp()
     - 

   * - PeekDown()
     - 

   * - PeekLeft()
     - 

   * - PeekRight()
     - 

   * - PeekDirection(Vector2 direction)
     - 
     