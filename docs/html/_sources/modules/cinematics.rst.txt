Cinematics
++++++++++

Create cinematic sequences to highlight special moments in your game.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Name
     - Name the cinematic for identification (optional).

   * - Trigger
     - If Trigger Once is enabled, the cinematic can only be activated once by the target. If Trigger is enabled, the 
       cinematic can be activated any number of times. If By Script is enabled, the cinematic can only be activated by a method call.

   * - LetterBox
     - Set the reference for the letterbox that will be activated to give the sequence a more cinematic feel. 
       This prefab can be found in the Assets/Prefab folder. 
       Drag and drop it into the scene and set the reference.

   * - On Begin
     - The Unity Event invoked when the cinematic begins.

   * - On Complete
     - The Unity Event invoked when the cinematic completes.
 
.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Targets
     - 

   * - Position
     - The position the camera will move to in sequence. 
       This value can be modified in the scene.

   * - Duration
     - The time it takes for the camera to get to the target's position.

   * - Wait
     - Once the camera arrives at its target, specify how long it waits there. If the toggle is enabled,
       the wait time is indefinite. To exit out of this state, call the following method: CinematicNextTarget();

   * - Zoom
     - Zoom the camera to a specified zoom level.

   * - On Arrival
     - The Unity Event invoked when the camera arrives at the target.

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Method
     - 

   * - CinematicTrigger (string cinematicName)
     - Trigger this cinematic.

   * - CinematicNextTarget ();
     - Move to the next cinematic target if the wait time at 
       the current one is indefinite.

LetterBox
=========

The letterbox will activate black bars that will tween into the camera view during a cinematic. The tweening values 
can be modified in the Let's Wiggle components attached to this gameobject. This is a tweening library that 
can be configured in the inspector. Simply change the time and tween settings for each MoveToY child tween.
