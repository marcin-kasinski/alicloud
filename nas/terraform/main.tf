
# ---------------
# Queries & outputs
# ---------------
data "template_file" "user_data" {
  template = file("${path.module}/user-data.conf")
}

data "alicloud_images" "centos" {
  #provider    = alicloud.worker_provider
  name_regex  = "^centos_7"
  most_recent = true
  owners      = "system"
}



resource "alicloud_instance" "instance" {
  image_id        = data.alicloud_images.centos.images[0].id
  instance_type   = "ecs.n1.tiny"
  #security_groups = concat([local.default_sg_id], var.security_groups)
  security_groups = [alicloud_security_group.default.id]

instance_name              = "mktest1"
system_disk_category       = "cloud_efficiency"
system_disk_size           = 40
description                = "mk test1"
internet_charge_type       = "PayByTraffic"
vswitch_id                 = "vsw-uf6kasgtw804zlxhbcgvl"
#tags                       = merge(local.default_tags, var.tags)
user_data                  = file("user-data.conf")
key_name                   = "marcin.kasinski"
#deletion_protection        = var.deletion_protection
}




output "images" {
  value = [data.alicloud_images.centos]
}
