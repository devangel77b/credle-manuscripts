#Connect computer to Tello via Tello's Wi-Fi
Drone=tello.Tello('', 8889) #open socket to Tello
self.thread = threading.Thread(target=self.videoLoop) #begin pulling video data
self.frame = self.tello.read() #read tello video frame
image = Image.fromarray(self.frame) #convert frame to image

self.panel.image = image #update GUI image
