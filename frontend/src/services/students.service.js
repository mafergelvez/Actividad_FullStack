import { api } from '@/lib/api';

export const studentsService = {
  getStudents: async () => {
    const response = await api.get('/students/');
    return response.data.results || response.data;
  },

  createStudent: async (data) => {
    const response = await api.post('/students/', data);
    return response.data;
  },

  uploadPicture: async (studentId, file) => {
    if (!studentId || !file) {
      throw new Error('Faltan datos para subir la imagen.');
    }

    const formData = new FormData();
    
    // TODO(actividad): Agregar el archivo en FormData con la clave correcta
    formData.append('profile_picture', file);

    try {
      // TODO(actividad): Consumir el action endpoint del backend
      // Usamos api.post enviando el formData y la URL dinámica
      const response = await api.post(`/students/${studentId}/upload-picture/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      return response.data;
    } catch (error) {
      // Manejo de errores para que se muestren en el modal rojo
      const message = error.response?.data?.detail || 'Error al subir la imagen';
      throw new Error(message);
    }
  }
};
