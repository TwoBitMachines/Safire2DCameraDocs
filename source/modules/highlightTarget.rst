Highlight Target
++++++++++++++++

On occasion there is a need to highlight an important game element by
having the camera follow it. This element is not the main target. It is also 
possible to follow the new target indefinitely and allow a certain range in which the main target can still
influence the camera.

Use this module to create predefined targets that can be triggered by some event and 
have the camera follow them. This requires the Follow module to be enabled.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Target
     - The target can either be a transform or a position. 
       Specify the follow speed.

   * - Duration
     - The total time the camera will follow the target. 
       If the toggle is enabled, the camera will follow the target indefinitely, or else it will revert to 
       following the main target automatically.

   * - Main Target Range
     - If the camera is following the target indefinitely, this value will specify the
       range in which the main target can still influence camera movement.

   * - Ignore Clamps
     - If enabled, the camera will be able to move through rooms while following the target.

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Method
     -

   * - HighlightTarget (string name)
     - 
 
   * - HighlightTargetTerminate ( )
     - 

   * - HighlightTarget (...)
     - If the highlight target hasn't been created in the inspector, you can still create one by code.
