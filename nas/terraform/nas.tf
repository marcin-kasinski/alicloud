resource "alicloud_nas_file_system" "foo" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "mk-testAccNasConfigFs"
}

resource "alicloud_nas_access_group" "foo" {
  name        = "mk-NasConfig"
  type        = "Classic"
  description = "mk-testAccNasConfig"
}

resource "alicloud_nas_mount_target" "foo" {
  file_system_id    = alicloud_nas_file_system.foo.id
  access_group_name = alicloud_nas_access_group.foo.id
}