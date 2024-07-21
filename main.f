PROGRAM ReadRealNumbers
    IMPLICIT NONE
  
    INTEGER,PARAMETER :: max_elements = 100
    REAL :: numbers(100)
    INTEGER :: num_elements, i
    CHARACTER(80) :: file_name
    CHARACTER(80) :: line
  
    ! Ask the user for the file name
    PRINT *, "Enter the name of the text file containing real numbers:"
    file_name = "File1.txt"
    !READ (*,*) file_name
  
    ! Open the file
    OPEN(UNIT=5, FILE=file_name, STATUS = 'OLD', ACTION='READ')
    ! Initialize the array size to 0
    num_elements = 0
  
    ! Read the numbers from the file
    DO
      READ(5,*) line
      READ(line, *) numbers(num_elements + 1)
      num_elements = num_elements + 1
    END DO
    ! Close the file
    CLOSE(5)
  
    ! Print the read numbers
    PRINT *, "Read ", num_elements, " real numbers from the file:"
    DO i = 1, num_elements
      PRINT *, numbers(i)
    END DO
    
END PROGRAM ReadRealNumbers