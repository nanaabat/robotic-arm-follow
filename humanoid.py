import pypot.vrep

poppy = pypot.vrep.from_vrep(config, vrep_host, vrep_port, vrep_scene)

poppy.walk.start()
