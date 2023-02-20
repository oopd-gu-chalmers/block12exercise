package edu.chalmers_gu_cse.oopd.exercises.polygonModel.shapes;

/**
 * Created by Niklas on 2016-02-19.
 */
public class PolygonFactory {
    public static Polygon createRectangle(int x, int y){
        return new Rectangle(x,y,4,2);
    }
    public static Polygon createTriangle(int x, int y){ return new Triangle(x,y,2,2); }
    public static Polygon createSquare(int x, int y){ return new Rectangle(x,y,2,2); }
}
