########################################################################################################################
# @ Module : Main Module
#
# @ Author : EMMA (Group I)
# @ Course : Computer Network
# @ Since  : January 2019
# @ Desc   : This Module  loads the client settings and start all the services ( distributor, requestor , collector...)
# @ Ref    : UJM | Computer Network Lab
#
#
########################################################################################################################

##################
# @ DEPENDENCIES
##################
# Loading Settings params ...
from project.player.app.core.distributor import Distributor

########################################################################################################################
#                                          MAIN   MODULE
########################################################################################################################

# Starting Distributor Service
Distributor.start_service(5001)

########################################################################################################################
#                                         END MAIN   MODULE
########################################################################################################################
