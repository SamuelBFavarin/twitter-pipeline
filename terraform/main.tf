provider "google" {
  credentials  = file("credentials/gcp-service-account-terraform-user.json")
  project = "twitter-pipeline-352822"
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_instance" "vm_instance" {
  name         = "twitter-producer-2"
  machine_type = "e2-micro"

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-bionic-v20220712"
    }
  }

  network_interface {
    # A default network is created for all GCP projects
    network = google_compute_network.vpc_network.self_link
    access_config {
    }
  }
}

resource "google_compute_network" "vpc_network" {
  name                    = "terraform-network"
  auto_create_subnetworks = "true"
}