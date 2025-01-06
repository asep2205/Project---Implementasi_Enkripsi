import imageio
import numpy as np
import matplotlib.pyplot as plt

def enkripsi_citra(citra, kunci):
  """
  Fungsi untuk mengenkripsi citra dengan menggunakan kunci.

  Args:
    citra: Citra yang akan dienkripsi.
    kunci: Kunci yang digunakan untuk enkripsi.

  Returns:
    Citra yang telah dienkripsi.
  """

  # Konversi citra ke array NumPy
  citra_array = np.array(citra)

  # Enkripsi setiap piksel dengan XOR kunci
  citra_enkripsi = citra_array ^ kunci

  # Kembalikan citra yang telah dienkripsi
  return citra_enkripsi

def dekripsi_citra(citra_enkripsi, kunci):
  """
  Fungsi untuk mendekripsi citra yang telah dienkripsi.

  Args:
    citra_enkripsi: Citra yang telah dienkripsi.
    kunci: Kunci yang digunakan untuk enkripsi.

  Returns:
    Citra yang telah didekripsi.
  """

  # Konversi citra yang telah dienkripsi ke array NumPy
  citra_array = np.array(citra_enkripsi)

  # Dekripsi setiap piksel dengan XOR kunci
  citra_dekripsi = citra_array ^ kunci

  # Kembalikan citra yang telah didekripsi
  return citra_dekripsi

# Memuat citra
citra = imageio.imread('citra.jpg')

# Menentukan kunci
kunci = 123

# Mengenkripsi citra
citra_enkripsi = enkripsi_citra(citra, kunci)

# Menyimpan citra yang telah dienkripsi
imageio.imwrite('citra_enkripsi.png', citra_enkripsi)

# Mendekripsi citra
citra_dekripsi = dekripsi_citra(citra_enkripsi, kunci)

# Menyimpan citra yang telah didekripsi
imageio.imwrite('citra_dekripsi.png', citra_dekripsi)

# Menampilkan citra asli, citra yang telah dienkripsi, dan citra yang telah didekripsi
plt.figure(figsize=(10, 5
