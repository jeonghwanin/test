m.def("python_hello",
      &c_hello, py::arg("name"));



python_hello(name)
