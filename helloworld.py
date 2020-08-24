#!/usr/bin/python

ef main(env, store_id):
    upc = "00000001"
    print("Hello, World!  {} {}".format(upc,store_id))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "param-1: [qa] or [prod] or [edge]\nparam-2: Store Id"
        exit() 
    if sys.argv[1]!="qa" and sys.argv[1]!="prod" and sys.argv[1]!="edge":
        print "env should be [qa] or [prod] or [edge]."
        exit()

    env = sys.argv[1]
    store_id = sys.argv[2]
    main(env, store_id)
