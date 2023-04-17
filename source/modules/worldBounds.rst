World Bounds
++++++++++++

World bounds are lines that clamp the camera's movement. They are a flexible
alternative to rooms when more precise control over camera movement is required.

An important aspect of these bounds is that they only come into effect when 
the player is within their boundaries. The camera will only be clamped once 
it has fully crossed the threshold of the bounds.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Direction
     - Specify if the bound clamps in the Left, Right, Top, or Bottom direction.

   * - Clamp
     - If Can Break Clamp is enabled, and the player moves to the other side of the
       bound, the bound will stop limiting the camera immediately. If it's disabled, the 
       bound will continue to restrict the camera even if the player crosses to the other side.