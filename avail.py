
class avail:
        cubo_semantico = None

        def _init_(self):
                self.cubo_semantico = {
                '=': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'error',
                                    'flotante': 'flotante'
                        }
                },
                '<': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '>': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '<=': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '>=': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '<>': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '==': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '*': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'flotante',
                                    'flotante': 'flotante'
                        }
                },
                '/': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'flotante',
                                    'flotante': 'flotante'
                        }
                }
                '-': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'flotante',
                                    'flotante': 'flotante'
                        }
                },
                '+': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'flotante',
                                    'flotante': 'flotante'
                        }
                },
                '%': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'flotante',
                                    'flotante': 'flotante'
                        }
                }
        }