Finite Parallax
++++++++++++++++

Create the illusion of depth by using several backgrounds to move with the camera. This parallax 
will not scroll infinitely. The edge of the background will be exposed if not properly hidden.

Each background can contain many child objects, and don't forget to set the layer order manually for each background.
Click the add button to add as many backgrounds as necessary.

.. note:: 
   If using a perspective camera, parallax comes for free! But you can still use this module to get infinite scrolling.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Transform Layer
     - The transform that will scroll with the camera.

   * - Parallax Rate
     - The rate at which the transform scrolls with the camera. A value approaching 1 is for the farthest layers.
       A value approaching 0 is for the layers nearest to the player. Values less than -1 are for foregrounds layers.

   * - Starting Offset
     - The offset applied to the transform layer during runtime to adjust for correct positioning if needed.

   * - Max Distance
     - The maximum distance the transform layer can scroll according to its parallax rate.

