CC=g++
LIBDIR = build

CFLAGS = -std=c++17 -Wall -Wextra -Werror

.PHONY: all clean tests style

STYLE = clang-format --style=google --verbose

all: topic_3 topic_4_2 topic_4_3

topic_3: $(patsubst %.cc, %.o, topic_3.cc)
	@$(CC) $(CFLAGS) topic_3.o -o $@
	@rm -rf *.o

topic_4_2: $(patsubst %.cc, %.o, topic_4_2.cc)
	@$(CC) $(CFLAGS) topic_4_2.o -o $@
	@rm -rf *.o

topic_4_3: $(patsubst %.cc, %.o, topic_4_3.cc)
	@$(CC) $(CFLAGS) topic_4_3.o -o $@
	@rm -rf *.o

topic_5_2: $(patsubst %.cc, %.o, topic_5_2.cc)
	@$(CC) $(CFLAGS) topic_5_2.o -o $@
	@rm -rf *.o

topic_5_3: $(patsubst %.cc, %.o, topic_5_3.cc)
	@$(CC) $(CFLAGS) topic_5_3.o -o $@
	@rm -rf *.o

test_3:
	@chmod +x test_3.sh
	@./test_3.sh

test_4_3:
	@chmod +x test_4_3.sh
	@./test_4_3.sh

test_5_2:
	@chmod +x test_5_2.sh
	@./test_5_2.sh

test_4_2: topic_4_2
	@./topic_4_2
	@./topic_4_2
	@./topic_4_2
	@./topic_4_2

clean:
	@rm -rf topic_3
	@rm -rf topic_4_2
	@rm -rf topic_4_3
	@rm -rf topic_5_2
	@rm -rf topic_5_3

is_style:
	$(STYLE) -n *.cc

style:
	$(STYLE) -i *.cc 