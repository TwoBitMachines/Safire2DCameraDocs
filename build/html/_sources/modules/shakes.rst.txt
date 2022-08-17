Shakes
++++++

This is an easy to use shake creator. The idea is to create shakes with predefined settings so they 
can be activated at runtime by name. Each shake can be called by a method or by using the shake trigger. 
Each shake that is created is actually linked to a Scriptable Object, which means you don't have 
to keep recreating the same shakes for each scene. As long as the Scriptable Object is referenced, the 
shakes will persist. In fact, the module won't work without this Scriptable Object. To create one, 
right click Create/FlareEngine/ShakesSO.

Any shake implemented will run simultaneously with all other shakes. The system will pool 
and recycle shakes to keep things nice an efficient.

Press the play button to test any shake while in Editor Mode.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Name
     - Name the shake for identification purposes.

   * - TimeScale
     -  If the shake uses time-scale, the shake can be affected by slow motion.

   * - Random
     - The camera abruptly shakes according to a random pattern.

   * - Perlin
     - Shake the camera with the perlin noise algorithm, resulting in a smoother and less chaotic
       shake.

   * - Sine
     - Shake the camera with a sinusoidal algorithm.

   * - One shot
     - The camera shakes in a single direction. This is a recoil. 
       This shake will need to be called by script since
       the shake direction can't be known ahead of time.

   * - Is Single Shake
     - These shakes are meant for high volumes short duration shakes such as bullet impacts.
       These shakes are grouped together and handled in a single state. The advantage is that these shakes are not
       added into the shake pool.

   * - Amplitude
     - This is the camera displacement in the horizontal and vertical axis. **The value Z is the angle displacement.**

   * - Speed
     - How fast the shake is implemented. Typically, a lower value is smoother, while a higher value if sharper.

   * - Strength
     - Shake intensity.

   * - Duration
     - How long the shake will last. The toggle button, if enabled, will make the shake last indefinitely. This is
       a constant shake and it must be turned off manually. Only one constant shake can run at a time.

.. list-table:: 
   :widths: 40 100
   :header-rows: 1

   * - Method
     - 

   * - Shake()
     - A convenient method for calling a normal sized shake.

   * - ShakeSmall()
     - A convenient method for calling a small shake.

   * - Shake(string shakeName)
     - Call the specified shake.

   * - ShakeType(...)
     - Create a shake through script. Call any of the different types.

   * - TurnOffConstantShake ( )
     -

   * - TurnOffAllShakes ( )
     -