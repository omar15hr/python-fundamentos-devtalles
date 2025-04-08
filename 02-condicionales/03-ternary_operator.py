is_student = False

if is_student:
  print("Licencia de estudiante")
else:
  print("licencia normal")


# True if condición else False

get_license = "Licencia de estudiante" if is_student else "Licencia normal"
print(get_license)