from core.logger import Logger

log = Logger()

log.write("Application Started")
log.write("Launching Chrome")
log.write("Waiting For Login")
log.write("Connected")
log.write("Opening Edit Page")
log.write("Ready")

log.close()