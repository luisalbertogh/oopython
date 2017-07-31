"""
oopython.py

OO Python sample project.
author: luisalbertogh@hotmail.com
"""

# Import classes from module
from mypackage import *;

# YAML & logging
import yaml;
import logging;
import logging.config;

# Oopython class
class Oopython:

	"""
	Main method
	"""
	def run(self):
		# Init logger
		logdict = yaml.load(open('config/log_config.yaml', 'r'));
		logging.config.dictConfig(logdict);
		logger = logging.getLogger('MyLogger');

		# New team
		mov = Team('Movistar', Cyclist('male','Spanish','Valverde'), Cyclist('male','Colombian','Quintana'), Cyclist('male','Basque','Izagirre'));
		logger.info(mov);
		logger.info('Num. de corredores: {0}'.format(mov.totalriders));

		# New team
		sky = Team('Sky', Cyclist('male','Basque','Landa'), Cyclist('male','Colombian','Henao'), Cyclist('male','Kenian','Froom'));
		logger.info(sky);
		logger.info('Num. de corredores: {0}'.format(mov.totalriders));

		# Add director
		mov.director = 'Unzue';
		logger.info(mov.director);

def main():
	oop = Oopython();
	oop.run();

if __name__ == "__main__":
	main();