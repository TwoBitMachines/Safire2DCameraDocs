Infinite Parallax
+++++++++++++++++

Create the illusion of depth by using several backgrounds to move with the camera. The 
parallax will scroll infinitely, even with a perspective camera.

Each background transform must contain a single sprite that is set to pivot center. 
Also, don't forget to set the layer order manually for each sprite in order to render the background images in correct order.
At runtime these backgrounds will be duplicated to achieve infinite parallax scrolling. Click the add button 
to add as many backgrounds as necessary.

.. note:: 
   If using a perspective camera, parallax comes for free! But you can still use this module to get infinite scrolling.

.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Transform Layer
     - The Transform that will scroll with the camera.

   * - Parallax Rate
     - The rate at which the transform scrolls with the camera. A value approaching 1 is for the farthest layers.
       A value approaching 0 is for the layers nearest to the player. Values less than -1 are for foregrounds layers.

   * - Auto Scroll
     - If this value is greater than zero, the transform will automatically move on its own. 
       This could be a layer that contains clouds. Try many parallax rates until you get one that gives a correct motion with the auto scroll.

.. warning:: 
   Infinite scrolling limitations: the camera size must always be smaller
   than the size of the image. If it isn’t, there will be noticeable gaps in each
   layer during scrolling. Things that can cause this are zooming the
   camera to a large value, a perspective camera that is too far away from
   the image layer, or a camera size that is simply too large. These issues
   may present themselves concurrently if not careful. Choose zoom levels wisely.
