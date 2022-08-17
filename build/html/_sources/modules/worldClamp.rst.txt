World Clamp
+++++++++++

The world clamp is a rectangle that encapsulates the entire game level and prevents 
the camera from moving outside of it. This is similar to rooms. However, while rooms can overlap,
they can't exist inside each other. This gets around that limitation.


.. list-table::
   :widths: 25 100
   :header-rows: 1

   * - Property
     - 

   * - Destination
     - The transform where the gameobject will be teleported to.

   * - LayerMask
     - Only gameobjects on this layer mask will be teleported.

   * - Delay
     - Add a time delay before teleporting.

   * - On Delay Start
     - The event invoked when the time delay begins. This only executes if delay is greater than zero.

   * - On Teleport
     - The event invoked when a gameobject is teleported.