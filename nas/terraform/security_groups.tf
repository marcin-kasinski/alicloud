resource "alicloud_security_group" "default" {
  name = "sg-mk-test"
  vpc_id              = "vpc-uf6qzufh526ho7l1cd5gp"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "22/22"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}