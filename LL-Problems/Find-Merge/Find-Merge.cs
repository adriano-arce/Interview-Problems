using System;
using System.Collections.Generic;

public class FindMergeSolution
{
    public class Node<T>
    {
        public T Value { get; set; }
        public Node<T> Next { get; set; }

        public Node(T value)
        {
            Value = value;
        }
    }

    public class LinkedList<T>
    {
        public Node<T> Head { get; set; }

        public LinkedList(T[] co)
        {
            collection.
            var curr = Head;
            foreach (var value in collection)
            {
                var newNode = new Node<T>(value);
                if (Head == null)
                {
                    curr = newNode;
                }
                else
                {
                    curr.Next = newNode;
                    curr = newNode;
                }
                curr = curr.Next;
            }
        }

        public override string ToString()
        {
            return base.ToString();
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

        Console.Write("\nPress any key to continue...");
        Console.ReadKey();
    }
}