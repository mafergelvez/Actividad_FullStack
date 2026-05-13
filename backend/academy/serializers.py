from rest_framework import serializers
from .models import Student, Instructor, Vehicle, Course, Enrollment, Lesson

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentPictureSerializer(serializers.ModelSerializer):
    def validate_profile_picture(self, value):
        # 1. Validar el tipo de archivo (MIME type)
        valid_mime_types = ['image/jpeg', 'image/png']
        if value.content_type not in valid_mime_types:
            raise serializers.ValidationError("Solo se permiten imágenes de tipo JPEG o PNG.")

        # 2. Validar el tamaño del archivo (2MB máximo)
        limit = 2 * 1024 * 1024  # 2 Megabytes
        if value.size > limit:
            raise serializers.ValidationError("La imagen es demasiado grande. El límite es de 2MB.")

        return value

    class Meta:
        model = Student
        fields = ['profile_picture']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
