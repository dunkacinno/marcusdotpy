import os
import shutil

print("File Organizer: Organize files into subdirectories based on their prefixes.")

try:
	# Get the directory of the script
	directory = os.path.dirname(os.path.abspath(__file__))

	# Iterate over all files in the directory
	for filename in os.listdir(directory):
		# Skip directories and the script file itself
		if os.path.isdir(os.path.join(directory, filename)) or filename == os.path.basename(__file__):
			continue

		try:
			# Separate the filename and its extension
			name, ext = os.path.splitext(filename)
			
			# Split the name at the first underscore
			parts = name.split("_", 1)
			if len(parts) > 1:
				subdirectory_name = parts[0]
				new_name = parts[1] + ext
			else:
				# If no underscore, put the file in an 'Unsorted' folder
				subdirectory_name = "Unsorted"
				new_name = filename

			# Create the subdirectory if it doesn't exist
			subdirectory = os.path.join(directory, subdirectory_name)
			if not os.path.exists(subdirectory):
				os.makedirs(subdirectory)

			# Construct the source and destination paths
			old_path = os.path.join(directory, filename)
			new_path = os.path.join(subdirectory, new_name)

			# Check for conflicts before copying
			if os.path.exists(new_path):
				raise FileExistsError(f"Conflict: {new_path} already exists.")

			# Copy the file to the new location
			shutil.copy2(old_path, new_path)  # Use copy2 to preserve metadata
			print(f"Copied: {filename} -> {new_path}")
		except Exception as e:
			print(f"Error processing {filename}: {e}")

except Exception as e:
	print(f"An unexpected error occurred: {e}")

print("All Done.")
