Zoom Trigger
++++++++++++

Once the target enters this trigger, the camera will begin to zoom.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Maintain
     - If the target exits the trigger, the zoom level will be maintained 
       until changed by another module.

   * - Revert On Exit
     - The zoom level will return to the original zoom level when the target exits the trigger.

   * - Scale
     - The zoom level.

   * - Smooth
     - The smoothing effect applied to the zoom.

   * - On Enter
     - The Unity Event invoked when the target enters the trigger.

   * - On Exit
     - The Unity Event invoked when the target exits the trigger.

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Method
     -

   * - Zoom (float scale, float duration)
     - 
 
   * - ZoomReset ( )
     - This will immediately reset the zoom to 1.

   * - ZoomSetToOne ( )
     - This will zoom the camera to 1, taking 1 second.
     