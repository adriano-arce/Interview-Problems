using System;
using System.Collections.Generic;

public class FindMergeSolution
{
    /// <summary>
    /// A simple Node class.
    /// 
    /// NOTE: Since Next has type Node&lt;T&gt; (a reference type), its default
    ///       value is null.
    /// </summary>
    /// <typeparam name="T">The type of Data.</typeparam>
    public class Node<T>
    {
        public T Data { get; set; }
        public Node<T> Next { get; set; }

        public Node(T data)
        {
            Data = data;
        }
    }

    /// <summary>
    /// Given the heads of two linked lists, returns the node where they merge
    /// (or null if they don't merge).
    /// </summary>
    /// <typeparam name="T"></typeparam>
    /// <param name="head1"></param>
    /// <param name="head2"></param>
    /// <returns></returns>
    public static Node<T> FindMerge<T>(Node<T> head1, Node<T> head2)
    {
        return null;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        //var testCases = new[]
        //{
        //};
        //var testCase = 0;
        //foreach (var t in testCases)
        //{
        //    Console.WriteLine("Test Case #{0}:", testCase);
        //    testCase++;
        //}
        var node = new Node<int>(5);
        Console.WriteLine(node);
        Console.WriteLine(node.Next == null ? "node.Next" : "None");
    }
}