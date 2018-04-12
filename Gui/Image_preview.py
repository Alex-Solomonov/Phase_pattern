from PyQt5.QtCore import Qt, QRectF, pyqtSignal, QT_VERSION_STR
from PyQt5.QtGui import QImage, QPixmap, QPainterPath
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog

class QtImageViewer(QGraphicsView):
	"""docstring for ClassName"""
	def __init__(self):
		super(QtImageViewer, self).__init__()

		self.scene = QGraphicsScene()
		self.setScene(self.scene)
		self.setMinimumSize(640, 320)

		self._pixmapHandle = None

	def pixmap(self):
		""" Returns the scene's current image pixmap as a QPixmap, or else None if no image exists.
		:rtype: QPixmap | None
		"""
		if self.hasImage():
			return self._pixmapHandle.pixmap()
		return None

	def image(self):
		""" Returns the scene's current image pixmap as a QImage, or else None if no image exists.
		:rtype: QImage | None
		"""
		if self.has_Image():
			return self._pixmapHandle.pixmap().toImage()
		return None

	def has_Image(self):
		# Returns whether or not the scene contains an image pixmap.
		return self._pixmapHandle is not None
		
	def clear_Image(self):
		# Removes the current image pixmap from the scene if it exists.
		if self.has_Image():
			self.scene.removeItem(self._pixmapHandle)
			self._pixmapHandle = None

	def set_Image(self, image):
		if type(image) is QPixmap:
			pixmap = image
		elif type(image) is QImage:
			pixmap = QPixmap.fromImage(image)
		else:
			image = QImage(image.tostring(),\
				image.shape[0],\
				image.shape[1],\
				image.shape[0],\
				QImage.Format_Mono)
		# else:
		# 	raise RuntimeError("ImageViewer.setImage: Argument must be a QImage or QPixmap.")
		if self.hasImage():
			self._pixmapHandle.setPixmap(pixmap)
		else:
			self._pixmapHandle = self.scene.addPixmap(pixmap)
		self.setSceneRect(QRectF(pixmap.rect()))  # Set scene size to image size.
		self.updateViewer()