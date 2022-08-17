Slow Motion Trigger
+++++++++++++++++++

Once the target enters this trigger, time scale will be slowed down.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Maintain
     - If the target exits the trigger, the slow motion effect will remain.

   * - Revert On Exit
     - The slow motion effect will be turned off when the target exits the trigger.

   * - Intensity
     - The value Time.timeScale will be set to.

   * - On Enter
     - The Unity Event invoked when the target enters the trigger.

   * - On Exit
     - The Unity Event invoked when the target exits the trigger.

.. list-table::
   :widths: 80 100
   :header-rows: 1

   * - Method
     -

   * - SlowMotion (float intensity, float duration, bool constant = false)
     -

   * - TurnOffSlowMotion ()
     -
