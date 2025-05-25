# Intentionally insecure configuration for testing
resource "google_storage_bucket" "example" {
  name     = "devsecops-test-bucket"
  location = "US"
  
  # FAIL: Public access allowed
  public_access_prevention = false
}

resource "google_compute_instance" "example" {
  name         = "devsecops-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  # FAIL: Missing disk encryption
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  # FAIL: Public IP exposure
  network_interface {
    network = "default"
    access_config {
      // Public IP will be assigned
    }
  }
  
  # FAIL: Missing secure boot
  shielded_instance_config {
    enable_secure_boot = false
  }
}

# FAIL: Insecure firewall rule
resource "google_compute_firewall" "allow_all" {
  name    = "allow-all"
  network = "default"

  allow {
    protocol = "all"
  }

  source_ranges = ["0.0.0.0/0"]
}

# FAIL: Insecure IAM policy
resource "google_storage_bucket_iam_member" "public_read" {
  bucket = google_storage_bucket.example.name
  role   = "roles/storage.objectViewer"
  member = "allUsers"
} 