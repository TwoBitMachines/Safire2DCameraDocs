Regions
+++++++

When the target enters a region, it will cause the camera to move
towards the center of the region. The farther the target moves inside the
region, the less influence it has on the camera. This requires the Follow module to be enabled.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Position
     - The region’s center can be a position in world space or a transform’s position.

   * - Outer Radius 
     - If the target is inside the outer region, both target and region will have influence over the camera.

   * - Inner Radius 
     - If the target is inside the inner region, the region will have complete control over the camera.

   * - Zoom
     - Zoom the camera as it moves closer to the region center with a specified smooth value. 
       If no zoom is desired, set to zero.

   * - Smooth
     - The smoothing effect applied to the zoom.

   * - On Enter
     - The Unity Event invoked when the target enters the region.

   * - On Exit
     - The Unity Event invoked when the target exits the region.
