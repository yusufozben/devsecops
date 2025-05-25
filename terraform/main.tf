# Intentionally insecure configuration for testing
resource "google_storage_bucket" "example" {
  name     = "devsecops-test-bucket"
  location = "US"
  
  # This will trigger Checkov security warnings
  versioning {
    enabled = false
  }
  
  # Missing encryption configuration
  # Missing public access prevention
}

resource "google_compute_instance" "example" {
  name         = "devsecops-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      # Missing disk encryption
    }
  }

  network_interface {
    network = "default"
    
    # This creates a public IP - security risk
    access_config {}
  }
  
  # Missing OS Login configuration
  # Missing secure boot
} 