output "bucket_name" {
  description = "The name of the created GCS bucket"
  value       = google_storage_bucket.example.name
}

output "instance_name" {
  description = "The name of the created compute instance"
  value       = google_compute_instance.example.name
}

output "instance_zone" {
  description = "The zone where the compute instance was created"
  value       = google_compute_instance.example.zone
}

output "instance_external_ip" {
  description = "The external IP address of the compute instance"
  value       = google_compute_instance.example.network_interface[0].access_config[0].nat_ip
} 