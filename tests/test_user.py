#!/usr/bin/env python3

import wrapper

def test_create_user():
  api = wrapper.Wrapper()

  api.createUser("testing")

  api.deleteUser("testing")
