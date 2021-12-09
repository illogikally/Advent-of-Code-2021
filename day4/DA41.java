import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import javax.sound.sampled.SourceDataLine;

public class DA41 {

  private static class Square {
    Integer value;
    Boolean isMarked = false;
    int x;
    int y;
    
    public Square(Integer value) {
      this.value = value;
    }
  } 

  private static class Board {
    private List<List<Square>> board;
    private HashMap<Integer, Square> map;
    private Integer totalValueSum = 0;
    private Integer markedValueSum = 0;
    private Integer latestMarkedValue = 0;
    private boolean isWon = false;
  
    public Board(List<List<Square>> board) {
      this.board = board;
      this.map = generateMap();
    }

    private HashMap<Integer, Square> generateMap() {
      HashMap<Integer, Square> map = new HashMap<>();

      for (int i = 0; i < board.size(); ++i) {
        for (int j = 0; j < board.get(0).size(); ++j) {
          Square square = board.get(i).get(j);
          square.x = j;
          square.y = i;
          map.put(square.value, square);
          this.totalValueSum += square.value;
        }
      }
      return map;
    }
  
    private boolean markAndCheckWin(Integer value) {
      Square square = map.get(value);

      if (square == null) {
        return false;
      }

      square.isMarked = true;
      markedValueSum += value;
      latestMarkedValue = value;

      if (rowCheck(square) || colCheck(square)) {
        isWon = true;
        return true;
      }

      return false;
    }

    private boolean rowCheck(Square square) {
      for (int i = 0; i < board.get(0).size(); ++i) {
        if (!board.get(square.y).get(i).isMarked) {
          return false;
        }
      }
      return true;
    }

    private boolean colCheck(Square square) {
      for (int i = 0; i < board.size(); ++i) {
        if (!board.get(i).get(square.x).isMarked) {
          return false;
        }
      }
      return true;
    }

    public Integer getFinalScore() {
      return (totalValueSum - markedValueSum) * latestMarkedValue;
    }
  }

  private static class Input {
    public List<Integer> numbers;
    public List<Board> boards;

    public Input() {}

    public Input(List<Integer> numbers, List<Board> boards) {
      this.numbers = numbers;
      this.boards = boards;
    }
  }

  static Input readInput(InputStream input) throws IOException{
    List<Integer> numbers = new LinkedList<>();
    List<Board> boards = new LinkedList<>();

    try (BufferedReader br = new BufferedReader(new InputStreamReader(input))) {
      numbers = Stream.of(br.readLine().split(","))
          .map(e -> Integer.parseInt(e))
          .collect(Collectors.toList());
      
      br.readLine();
      String line;
      List<List<Square>> board = new LinkedList<>();
      while((line = br.readLine()) != null) {
        if (line.isEmpty()) {
          boards.add(new Board(board));
          board = new LinkedList<>();
        }
        else {
          board.add(
            Stream.of(line.trim().split("\s+"))
                .map(e -> new Square(Integer.parseInt(e)))
                .collect(Collectors.toList())
          );
        }
      }
      boards.add(new Board(board));
    }
    return new Input(numbers, boards);
  }

  public static Integer part1(Input input) {
    for (var number : input.numbers) {
      for (var board : input.boards) {
        if (board.markAndCheckWin(number)) {
          return board.getFinalScore();
        }
      }
    }
    return null;
  } 

  public static Integer part2(Input input) {
    int boardWonCount = 0;
    for (var number : input.numbers) {
      for (var board : input.boards) {
        if (!board.isWon && board.markAndCheckWin(number)) {
          ++boardWonCount;
          if (boardWonCount == input.boards.size()) {
            return board.getFinalScore();
          }
        }
      }
    }
    return null;
  }

  public static void main(String[] args) {
    Input input = new Input();    
    try {
      var inputStream = new FileInputStream(new File("aoc4.input"));
      input = readInput(inputStream);
    }
    catch (IOException e) {} 

    System.out.println(part1(input));
    // System.out.println(endTime-startTime);
    // System.out.println(TimeUnit.NANOSECONDS.toMillis(endTime-startTime));

  }
}
