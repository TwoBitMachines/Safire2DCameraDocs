Look Ahead
++++++++++

The camera looks ahead in the direction of target movement. This requires the Follow module 
to be enabled.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Normal
     - The camera is always looking ahead.

   * - Recenter
     - The camera will stop looking ahead and revert once the target stops moving.

   * - Incremental
     - The camera will continue to look ahead only if the target is moving. 
       If the target is not moving, the camera will retain its position.

   * - Threshold
     - The camera will only look ahead if the target has reached the speed threshold. 
 
   * - Mouse
     - The look ahead direction will depend on the position of the mouse and not the target's direction. 

   * - Shape
     - If Square is enabled, the look ahead boundaries will be rectangular, defined by the Horizontal and Vertical values. 
       If Circle is enabled, the look ahead boundary will be a circle defined by the Radius value.

   * - Smooth
     - How quickly the camera should look ahead.
